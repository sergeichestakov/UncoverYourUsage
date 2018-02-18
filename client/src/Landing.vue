<template>
  <div>
    <b-jumbotron header="Take Back Control of Your Energy" lead="Analyze your energy usage and find ways to save.">
    </b-jumbotron>
    <section class="py-5">
      <div class="container">
        <h1>Describe your household:</h1>
        <b-form @submit.prevent="submit" v-if="!loading">
          <b-form-row>
            <b-col :key="id" v-for="(form, id) in formInfo" md="6" lg="4">
              <b-form-group :label="form.label" :label-for="id">
                <b-form-select v-if="form.type=='select'" :options="form.options" :id="id" v-model="form.data" />
                <b-form-input v-else :id="id" :type="form.type" v-model="form.data" />
              </b-form-group>
            </b-col>
          </b-form-row>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
        <loader v-else />
        <div v-if="error">{{error}}</div>
      </div>
    </section>
    <section v-if="prediction">
    </section>
  </div>
</template>

<script>
  import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
  export default {
    name: 'landing',
    components: {
      'loader': PulseLoader
    },
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        loading: false,
        error: null,
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
            label: "Air conditioner use in summer:",
            data: 1,
            type: "select",
            options: [
              {value: 1, text: "Turned on only a few days or nights when really needed"},
              {value: 2, text: "Turned on quite a bit"},
              {value: 3, text: "Turned on just about all summer"}
            ]
          },
          n_ncombath: {
            label: "Number of bathrooms",
            data: 0,
            type: "number"
          },
          n_typehuq: {
            label: "Type of housing unit",
            data:1,
            type:"select",
            options: [
              {value: 1, text: "Mobile Home"},
              {value: 2, text: "Single-Family Detached"},
              {value: 3, text: "Single-Family Attached"},
              {value: 4, text: "Apartment in Building with 2-4 Units"},
              {value: 5, text: "Apartment in Building with 5+ Units"}
            ]
          },
          n_temphome: {
            label: "Temperature when someone is at home (day)",
            data:0,
            type:"number"
          },
          n_cenachp: {
            label: "Central air conditioner is a heat pump?",
            data:0,
            type:"select",
            options: [
              {value: 0, text: "No"},
              {value: 1, text: "Yes"}
            ]
          },
          n_tempniteac: {
            label: "Temperature at night (summer)",
            data:0,
            type:"number"
          },
          n_agecdryer: {
            label: "Age of clothes dryer",
            data:1,
            type:"select",
            options:[
              {value: 1, text: "Less than 2 years old"},
              {value: 2, text: "2 to 4 years old"},
              {value: 3, text: "5 to 9 years old"},
              {value: 41, text: "10 to 14 years old"},
              {value: 42, text: "15 to 19 years old"},
              {value: 5, text: "20 years or older"}
            ]
          },
          n_naptflrs: {
            label: "Number of apartment floors",
            data:0,
            type:"number"
          },
          n_swimpool: {
            label: "Do you have a swimming pool?",
            data:0,
            type:"select",
            options: [
              {value:0, text: "No"},
              {value:1, text: "Yes"}
            ]
          },
          n_numcfan: {
            label: "Number of ceiling fans used",
            data:0,
            type:"number"
          },
          n_maintac: {
            label: "Maintenance performed on air conditioner:",
            data:0,
            type:"select",
            options: [
              {value: 0, text: "No"},
              {value: 1, text: "Yes"}
            ]
          },
          n_cooltype: {
            label: "Type of air conditioning equipment used:",
            data:1,
            type:"select",
            options: [
              {value: 1, text: 'Central system'},
              {value: 2, text: 'Window/wall units'},
              {value: 3, text: 'Both a central system and window/wall units'}
            ]
          },
        },
        prediction: null
      }
    },
    methods: {
      submit(){
        this.$http.post("/predict", this.formInfo).then(result => {
          this.loading = false;
        }, error => {
          console.error(error);
          this.error = error;
          this.loading = false;
        });
        this.loading = true;
      }
    }
  }

</script>

<style>


</style>
