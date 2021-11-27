<template>
<div class="grid-container">
  <header class="header" role="banner">
  <div class="header__search">Deployment Manager</div>

  <div class="header__avatar"><img class="img-responsive" width="109" height="42" src="./assets/site_logo.png"></div>
  </header>
  
  <main class="main">
    <div class='managment'>
      <br>
      <button class="button_stop" @click="stopCall()">
            Stop
      </button>
    </div>
      <dashboard-content   :replicas="replicas"  :alive="alive" :log_data="log_data"></dashboard-content>
  </main>
  <footer class="footer">
  <div class="footer__copyright">&copy; 2021</div>
  <div class="footer__signature">UC Davis</div>
  </footer>
</div>

</template>

<script>
import Content from './components/Content.vue'

export default {
  name: 'app',
  components: {
    'dashboard-content': Content
  },
  data () {
    return {
      replicas: {
        no_of_replicas: 4,
        replicas: ['Replica0', 'Replica1', 'Replica2', 'Replica3']
      },
      alive2: {
        status: {
          Replica0: 'Alive',
          Replica1: 'Alive',
          Replica2: 'Alive',
          Replica3: 'Dead',
        }
      },
      log_data: "Hello my name is Ashwin",
      alive: [
          {
              "id": "102969df9360f10f9b00627f35d1f414c167f1bbe208c3aa7d09de357cf81b4f",
              "name": "c1", // "cx" for clients, "sx" for replicas
              "short-id": "102969df93",
              "status": "running", // or "paused"
              "type": "client" // or "replica"
          }
        ],
    }
  },
  methods: {
    heartbeatAPI: async function() {
      var aliveApi =
        'http://0.0.0.0:5000/alive'
      this.completeAliveAPI = aliveApi;
      // console.log(aliveApi);
    },
    heartbeatCall: async function() {
      await this.heartbeatAPI();
      var axios = require('axios'); // for handling weather api promise
      var aliveApiResponse = await axios.get(this.completeAliveAPI);
      // console.log(aliveApiResponse);
      if (aliveApiResponse.status === 200) {
        this.alive = aliveApiResponse.data;
      } else {
        alert('Hmm... Seems like the server is down!');
      }
    },
    stopCall: async function() {
      var stopApi = 'http://0.0.0.0:5000/stop'
      var axios = require('axios'); // for handling weather api promise
      var stopApiResponse = await axios.post(stopApi);
      // console.log(aliveApiResponse);
      if (stopApiResponse.status === 200) {
        this.alive = stopApiResponse.data;
      } else {
        alert('Hmm... Seems like the server is down!');
      }
    },
    pollData: function(){
      setInterval(() => {
        this.heartbeatCall();
		    }, 1000)
    },
  },
  beforeDestroy () {
	  clearInterval(this.polling) 
  },
  created () {
	  this.pollData()
  },
  computed: {
  },
}
</script>

<style>
.grid-container {
    display: grid;
    grid-template-columns: 1fr; /* Side nav is hidden on mobile */
    grid-template-rows: 50px 1fr 50px;
    grid-template-areas:
      'header'
      'main'
      'footer';
    height: 100vh;
  }

.main-cards {
  column-count: 1;
  column-gap: 20px;
  margin: 20px;
}

/* Give every child element its grid name */
.header {
  grid-area: header;
  background-color: #341e74;
  color: white;
}

.sidenav {
  grid-area: sidenav;
  background-color: #394263;
}

.main {
  grid-area: main;
  background-color:  #D3D3D3;
}

.footer {
  grid-area: footer;
  background-color: #000000;
  color: white;
}

.management {
  margin-top: 50px;
  padding: 10px;
}


.button_stop {
  background: #cf142b;
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