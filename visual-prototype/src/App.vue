<script setup lang="ts">
import Node from "./components/Node.vue"
</script>



<template>
  <h1>Dataflow Prototype - Visual Editor</h1>

  <main>
    <Node title="Node Name" :inputs="['A', 'B', 'C']" :outputs="['X', 'Y']" :valid="false" :x="200" :y="100" />
    <Node title="Node Name" :inputs="['A', 'B', 'C']" :outputs="['X', 'Y']" :valid="false" :x="500" :y="700" />
    <Node title="Node Name" :inputs="['A', 'B', 'C']" :outputs="['X', 'Y']" :valid="false" :x="700" :y="1000" />
    <Node title="Node Name" :inputs="['A', 'B', 'C']" :outputs="['X', 'Y']" :valid="false" :x="1000" :y="1500" />
  </main>
</template>
