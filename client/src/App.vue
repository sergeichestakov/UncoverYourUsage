<template>
  <div>
    <b-navbar type="dark" toggleable="md" class="bg-dark">
      <div class="container">
        <a class="navbar-brand" href="#">Energy Saver</a>
        <b-navbar-toggle target="#navbarResponsive" aria-controls="navbarResponsive"
          aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </b-navbar-toggle>
        <b-collapse is-nav id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <router-link class="nav-link" to="/">My Energy
                <span class="sr-only">(current)</span>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/model">Science</router-link>
            </li>
          </ul>
        </b-collapse>
      </div>
    </b-navbar>
    <router-view></router-view>
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
    name: 'app'
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
