<template>
 <div style="position: relative;">
     <replica-chart :alive="alive"></replica-chart>
 </div>
</template>

<script>
import ReplicaChart from './ReplicaChart.vue';

export default {
 props: ['alive'],
 components: {
   'replica-chart': ReplicaChart
 },
}
</script>
