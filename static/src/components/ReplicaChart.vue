<template>
  <div>
      <div v-for="replica in alive" :key="replica.name">
          <div :onload="createNode(replica)"/>
      </div>
      
      <center><h2> Replicas </h2></center>
      <div class="main-overview" id="replica_grid">
      </div>

      <center><h2> Clients </h2></center>
      <div class="main-overview" id="client_grid">
      </div>
    </div>
</template>

<script>
export default {
  props: ["alive"],
  components: {},
  data() {
    
    return {
      isActive: false
    };
  },
  methods: {

    createNode: async function(replica) {
      if (document.contains(document.getElementById(replica.name))) {
            document.getElementById(replica.name).remove();
      }

      console.log("creating replica:", replica.name);
      var node = document.createElement("div");                 // Create a <div> node
      node.className = "deck";                                    // <div deck>


      var card = document.createElement("div");         // Create a text node
      card.className = "card";

      var title = document.createElement("div");         // Create a text node
      title.className = "card_title";

      var text = document.createTextNode(replica.name);

      if (replica.status == "running" ) {
          var card_data = document.createElement("div");
          card_data.className = "card_data";

          var img = document.createElement("img");
          img.className = "status_logo";
          img.src = "./src/assets/running.png";

          card_data.appendChild(img);

          var button = document.createElement('input');
          button.className = "button_custom";
          button.setAttribute('type', 'button'); // input element of type button
          button.setAttribute('value', 'PAUSE');
          button.addEventListener('click', this.pauseCall.bind(event, replica.id), false);

          card_data.appendChild(button);
      }
      else {
          var card_data = document.createElement("div");
          card_data.className = "card_data";

          var img = document.createElement("img");
          img.className = "status_logo";
          img.src = "./src/assets/stopped.png";

          card_data.appendChild(img);

          var button = document.createElement('input');
          button.className = "button_custom";
          button.setAttribute('type', 'button'); // input element of type button
          button.setAttribute('value', 'RESUME');
          button.addEventListener('click', this.resumeCall.bind(event, replica.id), false);
          card_data.appendChild(button);
      }

      title.appendChild(text);
      card.appendChild(title);
      card.appendChild(card_data);
      node.appendChild(card);                              // Append the text to <li>
      node.id = replica.name;

      if (replica.type == "client") {
        document.getElementById('client_grid').appendChild(node);
      }
      else {
        document.getElementById('replica_grid').appendChild(node);
      }
    },

    pauseAPI: function(replicaID) {
      console.log(replicaID);
      var pauseApi =
        'http://0.0.0.0:5000/pause/' + String(replicaID);
      this.completePauseAPI = pauseApi;
    },
    pauseCall: async function(replicaID) {
      await this.pauseAPI(replicaID);

      // document.getElementById(replicaName).className = "paused";

      var axios = require('axios'); // for handling weather api promise
      var pauseApiResponse = await axios.patch(this.completePauseAPI );
      console.log('Puase API called', replicaID);
      console.log(pauseApiResponse);
      if (pauseApiResponse.status === 200) {
        this.pauseData = pauseApiResponse.data;
      } else {
        alert('Hmm... Seems like the server is down!');
      }
    },
    resumeAPI: function(replicaID) {
      console.log(replicaID);
      var resumeApi =
        'http://0.0.0.0:5000/resume/' + String(replicaID);
      this.completeResumeAPI = resumeApi;
    },
    resumeCall: async function(replicaID) {
      await this.resumeAPI(replicaID);
      // document.getElementById(replicaName).className = "running";

      console.log('Resume API called', replicaID);
      var axios = require('axios'); // for handling weather api promise
      var resumeApiResponse = await axios.patch(this.completeResumeAPI );
      console.log(resumeApiResponse);
      if (resumeApiResponse.status === 200) {
        this.resumeData = resumeApiResponse.data;
      } else {
        alert('Hmm... Seems like the server is down!');
      }
    },
  },

};
</script>

<style>
.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 200px;
}

.box {
  padding: 30px;
  transition: transform .5s, box-shadow 1s;
}


.main-overview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(265px, 1fr)); /* Where the magic happens*/
  grid-auto-rows: auto;
  grid-gap: 10px;
  margin: 50px 200px 50px 200px;
}

.card_title{
  text-transform: uppercase;
  font-size: 20px;
  margin: 10px auto;
  color: aliceblue;
}

.card_data{
  text-transform: uppercase;
  font-size: 15px;
  margin-left: 40%;
  margin-right: auto;
  color: aliceblue;
}
.card_data_2{
  text-transform: uppercase;
  font-size: 15px;
  margin-left: 35%;
}

.deck{
  margin:15px;
  width:80%;
  height: auto;
  display: flex;
  position:relative;
  -webkit-perspective: 1000px;
  perspective: 1000px;
  font-family:verdana;
  border-radius:10px;
  /* box-shadow: 25px 25px 50px #1b1c1b, -25px -25px 50px #2d302f; */
  transition: 0.3s all ease-in-out;
}
.deck:hover{
  transform: scale(1.01) perspective(0px);
  box-shadow: 0 10px 10px rgba(10, 10, 10, 0.7);
}

.card{
  width:100%;
  height:100%;
  /* margin: 5px; */
  padding: 10px;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-transition: all .5s linear;
  transition: all .5s linear;
  border-radius:10px;
  background: #341e74;
}

.face {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  background-color:whitesmoke;  
  border-radius:10px;
}

.front{
  background-image:url('https://i.imgur.com/W3tra4F.gif');
  z-index:1;
  box-shadow: 5px 5px 5px #aaa;
}

.action_button {
  border-radius: 5px;
}

.status_logo {
  /* height: 10%; */
  max-width: 40%;
  height: auto;
}

/* CSS */
.button_custom {
  background: #5E5DF0;
  border-radius: 999px;
  /* box-shadow: #5E5DF0 0 10px 20px -10px; */
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  font-family: Inter,Helvetica,"Apple Color Emoji","Segoe UI Emoji",NotoColorEmoji,"Noto Color Emoji","Segoe UI Symbol","Android Emoji",EmojiSymbols,-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans",sans-serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 24px;
  opacity: 1;
  outline: 0 solid transparent;
  padding: 8px 18px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  width: fit-content;
  word-break: break-word;
  border: 0;
}
</style>
