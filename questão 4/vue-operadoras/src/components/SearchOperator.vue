<template>
  <div>
    <h1>Busca de Operadoras</h1>
    <input v-model="query" @input="searchOperadoras" placeholder="Digite o nome da operadora..." />
    <ul>
      <li v-for="operadora in operadoras" :key="operadora.codigo_operadora">
      {{ operadora.nome_operadora }} ({{ operadora.codigo_operadora }})
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SearchOperator', 
  data() {
    return {
      query: "",
      operadoras: []
    };
  },
  methods: {
    async searchOperadoras() {
      try {
        const response = await fetch(`http://127.0.0.1:5000/api/operadoras?query=${this.query}`);
        this.operadoras = await response.json();
      } catch (error) {
        console.error('Erro ao buscar operadoras:', error);
      }
    }
  }
};
</script>

<style scoped>
input {
  padding: 10px;
  margin-bottom: 10px;
  width: 100%;
  max-width: 400px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  background: #f5f5f5;
  margin: 5px 0;
  padding: 10px;
}
</style>
