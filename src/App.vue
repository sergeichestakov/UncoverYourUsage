<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="#">Energy Saver</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive"
          aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home
                <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">My Energy</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <b-jumbotron header="Take Back Control of Your Energy" lead="Analyze your energy usage and find ways to save.">
    </b-jumbotron>
    <section class="py-5">
      <div class="container">
        <h1>Describe your household:</h1>
        <b-form>
          <b-form-row>
            <b-col :key="id" v-for="(form, id) in formInfo" cols="4">
              <b-form-group :label="form.label" :label-for="id">
                <b-form-input :id="id" :type="form.type" v-model="form.data"/>
              </b-form-group>
            </b-col>
          </b-form-row>
        </b-form>
      </div>
    </section>
    <section v-if="prediction">
    </section>
    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Kaelan Mikowicz, Thomas Munduchira, Sergei Chestakov 2018</p>
      </div>
      <!-- /.container -->
    </footer>
  </div>
</template>

<script>
  export default {
    name: 'app',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        formInfo: {
          n_people: {
            label: "Number of people in your household:",
            data: 0,
            type: "number"
          },
          n_heaters: {
            label: "Number of heaters:",
            data: 0,
            type: "number"
          }
        }
      }
    },
    methods: {
      submit(){
        this.$http.post("/api/predict", this.formInfo).then(result => {
          
        }, error => {
          console.error(error);
        });
      }
    }
  }

</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  .container>h1 {
    margin-bottom: 1em;
  }

  .jumbotron {
    text-align: center;
    background: linear-gradient( rgba(255, 118, 0, 0.36),
    rgba(255, 118, 0, 0.36)),
    url('./assets/stanford.jpg');
    color: white;
    background-repeat: no-repeat;
    background-position: 50% 30%;
    background-size: cover;
    height: 30em;
    padding-top: 10em;
    border-radius: 0;
  }

  h1,
  h2 {
    font-weight: normal;
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

  input[type=number]::-webkit-inner-spin-button,
  input[type=number]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  input[type='number'] {
    -moz-appearance: textfield;
  }

</style>
