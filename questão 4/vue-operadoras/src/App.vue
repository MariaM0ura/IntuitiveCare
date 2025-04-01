<template>
  <div id="app">
    <SearchOperator /> <!-- Novo nome do componente -->
  </div>
</template>

<script>
// Atualize a importação para o novo nome
import SearchOperator from './components/SearchOperator.vue'

export default {
  name: 'App',
  components: {
    SearchOperator // Novo nome do componente
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
