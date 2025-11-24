<script setup lang="ts">
import Node from "./components/Node.vue"
import { ref, onMounted, type Ref } from "vue";

type PinID = {
  ownerId: string;
  pinName: string;
}

type NodeData = {
  id: string;
  tag: string;

  x: number;
  y: number;
}
type EdgeData = {
  source: PinID;
  sinks: Array<PinID>;
}

const nodes: Ref<{ [key: string]: NodeData; }> = ref({
  "node_1": { id: "node_1", tag: "literal", x: 200, y: 200 },
  "node_2": { id: "node_2", tag: "literal", x: 200, y: 600 },
  "node_3": { id: "node_3", tag: "logical_or", x: 500, y: 400 },
  "node_4": { id: "node_4", tag: "logical_and", x: 800, y: 600 },
  "node_5": { id: "node_5", tag: "print", x: 1100, y: 400 }
});

const edges: Ref<{ [key: string]: EdgeData; }> = ref({
  edge_1: { source: "node_1", sinks: ["node_3"] },
  edge_2: { source: "node_2", sinks: ["node_3", "node_4"] },
  edge_3: { source: "node_3", sinks: ["node_4"] },
  edge_4: { source: "node_4", sinks: ["node_5"] }
});

function getNodeCenter(nodeId: string) {
  const node = nodes.value[nodeId];
  if (node === undefined) {
    return
  }
  return { x: node.x, y: node.y };
}
</script>



<template>
  <main>
    <h1>Dataflow Prototype - Visual Editor</h1>
    <Node title="Literal" :inputs="[]" :outputs="['Value']" :id="'node_1'" :x="200" :y="200" />
    <Node title="Literal" :inputs="[]" :outputs="['Value']" :id="'node_2'" :x="200" :y="600" />
    <Node title="Or" :inputs="['A', 'B']" :outputs="['Result']" :id="'node_3'" :x="500" :y="400" />
    <Node title="And" :inputs="['A', 'B']" :outputs="['Result']" :id="'node_4'" :x="800" :y="600" />
    <Node title="Print" :inputs="['In']" :outputs="[]" :id="'node_5'" :x="1100" :y="400" />
  </main>
</template>
