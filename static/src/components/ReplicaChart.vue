<template>
  <div>
    <div class="main-overview">
      <div class="deck" v-for="replica in alive" :key="replica.name" :id="replica.name">
        <div class="card">
          <div class="card_title">{{replica.name }}</div>
            
          <div v-if="replica.status == 'running'">
            <!-- <div class="overviewcard__info">{{replica.status}}</div> -->
          <div class="card_data">
            <img class = "status_logo" src="../assets/running.png" >
          </div>

          <div class="card_data_2">
            <button class="button_custom" @click="pauseCall(replica.id, replica.name)">
                  Pause
            </button>
          </div>
          </div>

          <div v-else>
            <div class="card_data">
              <img class = "status_logo" src="../assets/stopped.png" >
            </div>

            <div class="card_data_2">
              <button class="button_custom" @click="resumeCall(replica.id, replica.name)">
                    Resume
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["replicas", "alive"],
  components: {},
  data() {
    
    return {
      isActive: false
    };
  },
  methods: {
    pauseAPI: function(replicaID) {
      console.log(replicaID);
      var pauseApi =
        'http://0.0.0.0:5000/pause/' + String(replicaID);
      this.completePauseAPI = pauseApi;
    },
    pauseCall: async function(replicaID, replicaName) {
      await this.pauseAPI(replicaID);

      // document.getElementById(replicaName).className = "paused";

      var axios = require('axios'); // for handling weather api promise
      var pauseApiResponse = await axios.patch(this.completePauseAPI );
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
    resumeCall: async function(replicaID, replicaName) {
      await this.resumeAPI(replicaID);
      // document.getElementById(replicaName).className = "running";

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
