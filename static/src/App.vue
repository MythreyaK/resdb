<template>
<div class="grid-container">
  <header class="header">
  <div class="header__search">Deployment Manager</div>
  <div class="header__avatar"><img class="img-responsive" width="109" height="42" src="./assets/site_logo.png"></div>
  
  </header>


  <aside class="sidenav"></aside>
  <main class="main">
      <button id="search-btn" @click="heartbeatCall">
              Refresh
      </button>
      <dashboard-content   :replicas="replicas"  :alive="alive"></dashboard-content>
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
      console.log(aliveApi);
    },
    heartbeatCall: async function() {
      await this.heartbeatAPI();
      var axios = require('axios'); // for handling weather api promise
      var aliveApiResponse = await axios.get(this.completeAliveAPI);
      console.log(aliveApiResponse);
      if (aliveApiResponse.status === 200) {
        this.alive = aliveApiResponse.data;
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
	  // this.pollData()
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
  
.sidenav {
  display: none;
  grid-area: sidenav;
  background-color: #394263;
}

.main-cards {
  column-count: 1;
  column-gap: 20px;
  margin: 20px;
}

/* Give every child element its grid name */
.header {
  grid-area: header;
  background-color: #000000;
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
</style>