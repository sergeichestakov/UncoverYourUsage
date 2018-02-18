<template>
  <div>
    <b-jumbotron header="Take Back Control of Your Energy" lead="Analyze your energy usage and find ways to save.">
    </b-jumbotron>
    <section class="py-5">
      <div class="container">
        <h1>Describe your household:</h1>
        <b-form @submit.prevent="submit">
          <b-form-row>
            <b-col :key="id" v-for="(form, id) in formInfo" md="4">
              <b-form-group :label="form.label" :label-for="id">
                <b-form-select v-if="form.type=='select'" :options="form.options" :id="id" v-model="form.data" />
                <b-form-input v-else :id="id" :type="form.type" v-model="form.data" />
              </b-form-group>
            </b-col>
          </b-form-row>
          <b-button type="submit" variant="primary">Submit</b-button>
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
          n_totcsqft: {
            label: "Total cooled square footage:",
            data: 0,
            type: "number"
          },
          n_acrooms: {
            label: "Number of rooms cooled:",
            data: 0,
            type: "number"
          },
          n_bedrooms: {
            label: "Number of bedrooms:",
            data: 0,
            type: "number"
          },
          n_washload: {
            label: "Number of washes per week",
            data: 0,
            type: "number"
          },
          n_usecenac: {
            label: "Frequency per week central air conditioner used in summer ",
            data:0,
            type:"number"
          },
          n_ncombath: {
            label: "Number of bathrooms",
            data: 0,
            type: "number"
          },
          n_typehuq: {
            label: "Type of housing unit",
            data:0,
            type:"number"
          },
          n_usecenac: {
            label: "Per week central air conditioner use in summer ",
            data:0,
            type:"number"
          },
          n_temphome: {
            label: "Temperature when someone is at home during the day",
            data:0,
            type:"number"
          },
          n_cenachp: {
            label: "Central air conditioner is a heat pump?",
            data:0,
            type:"number"
          },
          n_tempniteac: {
            label: "Temperature at night(summer)",
            data:0,
            type:"number"
          },
          n_agecdryer: {
            label: "Age of clothes dryer",
            data:0,
            type:"number"
          },
          n_naptflrs: {
            label: "Number of apartment floors",
            data:0,
            type:"number"
          },
          n_swimpool: {
            label: "Do you have a swimming pool?",
            data:0,
            type:"number"
          },
          n_numcfan: {
            label: "Number of ceiling fans used",
            data:0,
            type:"number"
          },
          n_maintac: {
            label: "Maintenance performed on air conditioner:",
            data:0,
            type:"number"
          },
          n_cooltype: {
            label: "Type of air conditioning equipment used:",
            data:0,
            type:"number"
          },
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
