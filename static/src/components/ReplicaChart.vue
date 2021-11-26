<template>
  <div>
    <div class="main-overview">
      <div class="overviewcard" v-for="(replica, index) in alive.status" :key="index">
        <div class="overviewcard__icon">{{index }}</div>
        <div class="overviewcard__info">{{replica}}</div>
      </div>
      <p> Total deployed replicas: {{replicas.no_of_replicas}} </p>
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
}
</style>
