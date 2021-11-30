<template>
    <div v-if="alive.length !== 0" class="items-container" style="padding: 20px; background: rgb(239 239 239); border-radius: 20px;">
     <div  v-for="node of sortedNodes" :key="node.id" style="width: 33%; display: flex; justify-content: center; ">
        <node-item :node="node" ></node-item>  
     </div>
    </div>
</template>

<script>
import "./NodeItem.vue"
import NodeItem from './NodeItem.vue';
export default {
  props: ["alive"],
  components: {NodeItem},
  data() {
    
    return {
      isActive: false,
    };
  },
  mounted() {
    console.log(this.sortedNodes);
  },
  computed: {
      sortedNodes() {
        return this.alive.sort((a, b) => {
            const aID = parseInt(a.name.substr(1));
            const bID = parseInt(b.name.substr(1));
            if(a.name.startsWith("s") && b.name.startsWith("s")) {
              return aID > bID ? 1 : -1;
            }
            if(a.name.startsWith("c") && b.name.startsWith("c")) {
              return aID > bID ? 1: -1;
            }
            if(a.name.startsWith("s")) {
              return -1;
            }
            return 1;
        });
      }
  },

};
</script>

<style scoped>
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

.items-container {
  display: flex;
  flex-wrap: wrap;
}
</style>
