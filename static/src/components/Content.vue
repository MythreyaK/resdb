<template>
 <div style="position: relative;">
     <replica-chart :replicas="replicas" :alive="alive"></replica-chart>
 </div>
</template>

<script>
import ReplicaChart from './ReplicaChart.vue';

export default {
 props: ['replicas', 'alive'],
 components: {
   'replica-chart': ReplicaChart
 },
}
</script>
