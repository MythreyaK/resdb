<template>
    <div style="margin: 20px 10px">
      <div class="item" :class="{client: !isReplica}">
        <div>{{readableName}}</div>
        <div class="status">
          <div class="status-dot" :class="{running: node.status==='running'}"></div>
          {{node.status==="running"?"Running":"Stopped"}}
        </div>
        <v-icon @click.native="toggle" class="action-icon" color="white">
      {{node.status === "running" ? 'mdi-cancel': 'mdi-play'}}
    </v-icon>
    </div>
      </div>
</template>

<script>
export default {
  props: ["node"],
  name: "NodeItem",
  computed: {
    isReplica() {
        return this.node.type === "replica";
    },
    readableName() {
      if(this.isReplica) {
        return `Replica #${this.node.name.substr(1)}`;
      } else {
        return `Client #${this.node.name.substr(1)}`;
      }
    }
  },
  methods: {
    toggle() {
      if(this.node.status === "running") {
        this.pause();
      } else this.resume();
    },
    async pause() {
      var pauseApi =
        `http://${window.location.host.split(":")[0]}:5000/pause/` + String(this.node.id);
      // document.getElementById(replicaName).className = "paused";

      var axios = require('axios'); // for handling weather api promise
      var pauseApiResponse = await axios.patch(pauseApi);
      console.log(pauseApiResponse);
      if (pauseApiResponse.status === 200) {
       ///this.pauseData = pauseApiResponse.data;
      } else {
        alert('Hmm... Seems like the server is down!');
      }
    },
    async resume() {
      var resumeAPI =
        `http://${window.location.host.split(":")[0]}:5000/resume/` + String(this.node.id);
      // document.getElementById(replicaName).className = "running";

      var axios = require('axios'); // for handling weather api promise
      var resumeApiResponse = await axios.patch(resumeAPI);
      console.log(resumeApiResponse);
      if (resumeApiResponse.status === 200) {
        //this.resumeData = resumeApiResponse.data;
      } else {
        alert('Hmm... Seems like the server is down!');
      }
    }
  }
};
</script>

<style scoped>
  .item {
    width: 180px;
    height: 180px;
    display: flex;
    flex-direction: column;
    font-weight: 600;
    justify-content: center;
    align-items: center;
    background: #341e74;
    color: #fff;
    border-radius: 20px;
    position: relative;
  }

  .item.client {
    background: #1e6474;
  }

  .status {
    font-size: 13px;
    font-weight: 400;
    position: absolute;
    bottom: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    right: 15px;
  }

  .status-dot {
    width: 10px;
    height: 10px;
    background: #f72323;
    border-radius: 20px;
    margin-right: 4px;
  }

    .status-dot.running {
    background: #05d728;
  }

  .action-icon {
    position: absolute;
    top: 10px;
    left: 10px;
    font-size: 19px;
    cursor: pointer;
  }
</style>
