
console.log("Hello from main 2 !")
console.log("Who start stream: ",whoStartStream)


const localVideo = document.getElementById('local-video');
const remoteDiv = document.getElementById('remote-videos')
const startButton = document.getElementById('start-button');

const remoteVideo = document.createElement('video');


let servers = {
    iceServers:[
        {
            urls:['stun:stun1.1.google.com:19302', 'stun:stun2.1.google.com:19302']
        }
    ]
}




const socket = new WebSocket('ws://localhost:8000/ws/chat/' + chatRoom + '/');
const peerConnection = new RTCPeerConnection(servers);

let userMediaStream = new MediaStream();


const videoConstraintsMinim = {
  audio: false,
  video: {
    width: { max: 5 },     // Set the maximum width of the video
    height: { max: 5 },    // Set the maximum height of the video
    frameRate: { max: 1 },  // Set the maximum frame rate of the video
  }
};


async function takeMedia() {
                if (user != "some_user") {
         userMediaStream = await navigator.mediaDevices.getUserMedia({
              audio: true,
              video: true
            });   } else {userMediaStream = await navigator.mediaDevices.getUserMedia(videoConstraintsMinim)}

             userMediaStream.getTracks().forEach(track => {
             peerConnection.addTrack(track, userMediaStream);
                     });
             localVideo.srcObject = userMediaStream;

    }



function stopStreamedVideo(videoElem) {
  const stream = videoElem.srcObject;
  const tracks = stream.getTracks();

  tracks.forEach((track) => {
    track.stop();
  });

  videoElem.srcObject = null;
  videoElem.remove()
}



async function sendOffer() {
        const offer = await peerConnection.createOffer()

        peerConnection.setLocalDescription(offer);
        socket.send(JSON.stringify({
            peer:user,
            event:"offer",
            data:offer
        }))
       }


async function sendCandidate() {
          peerConnection.onicecandidate = event => {
            socket.send(JSON.stringify({
            peer:user,
            event:"candidate",
            data:event.candidate
        }))
        }
    }


async function listenTrackToRemote() {
  peerConnection.addEventListener('track', event => {
    remoteVideo.autoplay = true;
    console.log('Got remote stream', event);
    remoteStream = event.streams[0];
    remoteVideo.srcObject = remoteStream;
    remoteDiv.appendChild(remoteVideo);
  });

}





  socket.onopen = async (event) => {
        console.log("Websocket connection opened...")
        socket.send(JSON.stringify({"user_connected":user}))
        socket.send(JSON.stringify({"first_click":user}))
        sendOffer();sendCandidate();takeMedia();listenTrackToRemote();startButton.remove()

        //startButton.addEventListener("click", () => {socket.send(JSON.stringify({"first_click":user}))})
       // startButton.addEventListener("click", () => {sendOffer();sendCandidate();takeMedia();listenTrackToRemote();startButton.remove()})


}





socket.onmessage =async (event) => {
        var content = JSON.parse(event.data)
        var data = content.data.data



        whoStartStream = content.data.first_click
        userConnected = content.data.user_connected



        if (content.data.peer === user) {return;}

 switch (content.data.event) {
        case ("offer"):

            console.log("answer on offer")

            peerConnection.setRemoteDescription(data)

            const answer = await peerConnection.createAnswer();
            console.log("Answer:",answer)

            await peerConnection.setLocalDescription(answer)
            socket.send(JSON.stringify({
                peer:user,
                event:"answer",
                data:answer
            }))

            break;

        case ("answer"):
            console.log("answer on answer")
            await peerConnection.setRemoteDescription(data)

            if (user == "Anton") {
            stopStreamedVideo(localVideo) }

            break;

        case ("candidate"):
            console.log("answer on candidate")
            peerConnection.addIceCandidate(data)

            break;
    }

};


socket.onclose = (event) => {
        console.log("Websocket closed...")
};


//if (whoStartStream != "None") {if (user != whoStartStream) {}}
takeMedia();listenTrackToRemote();startButton.remove()

localVideo.muted = true;
