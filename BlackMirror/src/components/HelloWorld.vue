<template>
  <div class="hello">
    <button @click="getInfo">정보 받아오기 </button>
    <table>
      <thead>

      </thead>
      <tbody>
        <tr v-for="(tr, i) in data" :key="i">
          <td v-if="tr">
            {{tr[0]}}
          </td>
          <td v-if="tr">
            {{tr[1]}}
          </td>
          <td v-if="tr">
            {{tr[2]}}
          </td>
          <td v-if="tr">
            {{tr[3]}}
          </td>
          <td v-if="tr">
            {{tr[4]}}
          </td>
          <td v-if="tr">
            {{tr[5]}}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  sockets: {
    connect: function(){
      console.log('socket connected')
    },
    mise: function(a){
      console.log('get mise')
      console.log(a)
      this.data = a.data
    }
  },
  props: {
    msg: String
  },
  data () {
    return {
      data: null
    }
  },
  methods: {
    getInfo: function(){
      this.$socket.emit('mise')
      console.log('getMise called')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
