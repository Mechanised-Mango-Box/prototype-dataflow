<template>
    <div 
        class="node" 
        :style="{ top: y + 'px', left: x + 'px', position: 'absolute' }"
    >
        <header>{{ title }}</header>
        <div class="node-body">
            <div class="input">
                <p v-for="(inp, i) in inputs" :key="i">{{ inp }}</p>
            </div>
            <div class="output">
                <p v-for="(out, i) in outputs" :key="i">{{ out }}</p>
            </div>
        </div>
        <footer>Valid: {{ valid ? 'YES' : 'NO' }}</footer>
    </div>
</template>

<script setup lang="ts">
defineProps<{
    title: string
    inputs: string[]
    outputs: string[]
    valid: boolean
    x: number
    y: number
}>()
</script>

<style scoped>
.node {
    border: 1px solid black;
    display: inline-block;
}

.node-body {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.input,
.output {
    display: flex;
    flex-direction: column;
    text-align: center;
}
</style>
