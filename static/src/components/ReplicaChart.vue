<template>
  <div>
    <div class="main-overview">
      <div class="overviewcard" v-for="replica in alive" :key="replica">
        <div class="overviewcard__icon">{{replica.name }}</div>
        <div v-if="replica.status == 'running'">
          <div class="overviewcard__info">{{replica.status}}</div>
          <img class = "status_logo" src="../assets/running.png" >
        </div>
        <div v-else>
          <div class="overviewcard__info">{{replica.status}}</div>
          <img class = "status_logo" src="../assets/stopped.png">
        </div>

        <button class="action_button" @click="pauseCall(replica.id)">
              Pause
        </button>

        <button class="action_button" @click="resumeCall(replica.id)">
              Resume
        </button>
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

    };
  },
  methods: {
    pauseAPI: function(replicaID) {
      console.log(replicaID);
      var pauseApi =
        'http://0.0.0.0:5000/pause/' + String(replicaID);
      this.completePauseAPI = pauseApi;
    },
    pauseCall: async function(replicaID) {
      await this.pauseAPI(replicaID);
      var axios = require('axios'); // for handling weather api promise
      var pauseApiResponse = await axios.post(this.completePauseAPI );
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
      var axios = require('axios'); // for handling weather api promise
      var resumeApiResponse = await axios.post(this.completeResumeAPI );
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

.overviewcard:hover {
  transform: scale(1.01) perspective(0px);
  box-shadow: 0 10px 10px rgba(10, 10, 10, 0.7);
}

.main-overview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(265px, 1fr)); /* Where the magic happens */
  grid-auto-rows: 94px;
  grid-gap: 20px;
  margin: 20px;
}

.overviewcard {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #6577B3;
  border-radius: 10px;
}

.action_button {
  border-radius: 5px;
}

.status_logo {
  /* height: 10%; */
  max-width: 40%;
  height: auto;
}
</style>
