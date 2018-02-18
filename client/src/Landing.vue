<template>
  <div>
    <b-jumbotron header="Take Back Control of Your Energy" lead="Analyze your energy usage and find ways to save.">
    </b-jumbotron>
    <section class="py-5">
      <div class="container">
        <h1>Describe your household:</h1>
        <b-form>
          <b-form-row>
            <b-col :key="id" v-for="(form, id) in formInfo" cols="4">
              <b-form-group :label="form.label" :label-for="id">
                <b-form-input :id="id" :type="form.type" v-model="form.data" />
              </b-form-group>
            </b-col>
          </b-form-row>
        </b-form>
      </div>
    </section>
    <section v-if="prediction">
    </section>
  </div>
</template>

<script>
  export default {
    name: 'landing',
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
        },
        prediction: null
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


</style>
