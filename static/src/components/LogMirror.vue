<template>
    <div class='scroll-box'>
    {{ log_data }}
    </div>
</template>

<script>
export default {
  props: ["log_data"],
  components: {},
  data() {
    return {

    };
  },
  methods: {
      getLog: function() {
          console.log('in fetch');
        fetch('http://0.0.0.0:5000/logstream')
        .then(response => response.body)
        .then(res => res.on('readable', () => {
        let chunk;
        while (null !== (chunk = res.read())) {
            console.log(chunk.toString());
        }
        })).catch(err => console.log(err));
        //   fetch('')
        //     .then(response=> {
        //     const reader = response.getReader()
        //     let data = []
        //     return reader.read().then(read = (result)=>{
        //         if(result.done){
        //             return data
        //         }

        //         data.push(result.value)
        //         return reader.read().then(read)
        //     })
        //     })
        //     .then(data => {
        //         // Do whatever you want with your data
        //         this.log_data = data;
        //     })

            // const axios = require('axios');
            // const res = await axios.get('https://images.unsplash.com/photo-1506812574058-fc75fa93fead', {
            //     responseType: 'stream'
            // });

            // // const fs = require('fs');
            // // res.data.pipe(fs.createWriteStream('./south-beach.jpg'));
      },

  },
  created() {
      this.getLog();
  }

};
</script>

<style>
/* Box styles */
.scroll-box {
border: none;
padding: 5px;
font: 24px/36px sans-serif;
width: auto;
height: 100%;
overflow: scroll;
}

/* Scrollbar styles */
/* ::-webkit-scrollbar {
width: 12px;
height: 12px;
}

::-webkit-scrollbar-track {
box-shadow: inset 0 0 10px olivedrab;
border-radius: 10px;
}

::-webkit-scrollbar-thumb {
border-radius: 10px;
background: yellowgreen; 
box-shadow: inset 0 0 6px rgba(0,0,0,0.5); 
}

::-webkit-scrollbar-thumb:hover {
background: #7bac10;
} */
</style>
