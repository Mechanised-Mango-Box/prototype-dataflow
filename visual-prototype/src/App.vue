<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<style scoped>
</style>


<template>
  <header>Dataflow Prototype - Visual Editor</header>

  <main>
    <div>
      <table>
        <caption>
          Node Name
        </caption>
        <thead>
          <tr>
            <th>In Pin</th>
            <th>In Name</th>
            <th>Gap</th>
            <th>Out Name</th>
            <th>Out Pin</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><button>*</button></td>
            <td>A</td>
            <td></td>
            <td>X</td>
            <td><button>*</button></td>
          </tr>
          <tr>
            <td><button>*</button></td>
            <td>B</td>
            <td></td>
            <td>Y</td>
            <td><button>*</button></td>
          </tr>
          <tr>
            <td><button>*</button></td>
            <td>C</td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        </tbody>
      </table>

    </div>
  </main>
</template>
