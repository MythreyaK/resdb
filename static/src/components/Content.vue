<template>
 <div style="position: relative;">
     <replica-chart :replicas="replicas" :alive="alive"></replica-chart>
     <hr>
     Logs:
     <hr>
     <log-mirror :log_data="log_data"></log-mirror>
 </div>
</template>

<script>
import ReplicaChart from './ReplicaChart.vue';
import LogMirror from './LogMirror.vue';

export default {
 props: ['replicas', 'alive', 'log_data'],
 components: {
   'replica-chart': ReplicaChart,
   'log-mirror': LogMirror
 },
}
</script>
