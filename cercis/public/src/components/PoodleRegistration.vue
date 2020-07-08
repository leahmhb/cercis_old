<template>
  <div id="registration">
    <article v-if=!showForm class="mt-2">
      <div class="row">
        <div class="col">
          <table class="table table-sm">
            <tbody>
              <tr>
                <th>AKC</th>
                <td>{{ poodle.akc }}</td>
              </tr>
              <tr>
                <th>CHIC</th>
                <td>{{ poodle.chic }}</td>
              </tr>
              <tr>
                <th>AKC DNA</th>
                <td>{{ poodle.akc_dna }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col">
          <table class="table table-sm">
            <tbody>
              <tr>
                <th>UKC</th>
                <td>{{ poodle.ukc }}</td>
              </tr>
              <tr>
                <th>Addtl</th>
                <td>{{ poodle.addtl }}</td>
              </tr>
              <tr>
                <th>Pedigree Source</th>
                <td>
                  <a :href="poodle.pedigree_src">#</a>                  
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </article>
    <article v-else>
      <form :id="formRef" :ref="formRef" method="post" @submit.prevent="changePoodle(formRef)">

        <b-form-group label="AKC" label-for="akc">
          <b-form-input id="akc" v-model="poodle.akc" trim></b-form-input>
        </b-form-group>

        <b-form-group label="UKC" label-for="ukc">
          <b-form-input id="ukc" v-model="poodle.ukc" trim></b-form-input>
        </b-form-group>

        <b-form-group label="CHIC" label-for="chic">
          <b-form-input id="chic" v-model="poodle.chic" trim></b-form-input>
        </b-form-group>

        <b-form-group label="Addtl" label-for="addtl">
          <b-form-input id="addtl" v-model="poodle.addtl" trim></b-form-input>
        </b-form-group>

        <b-form-group label="AKC DNA" label-for="akc_dna">
          <b-form-input id="akc_dna" v-model="poodle.akc_dna" trim></b-form-input>
        </b-form-group>

        <b-form-group label="Pedigree Source" label-for="pedigree_src">
          <b-form-input id="pedigree_src" v-model="poodle.pedigree_src" trim></b-form-input>
        </b-form-group>

      </form>

    </article>

    <div v-if="perms.core.change_poodle" class="mt-4 mb-0 d-flex flex-row justify-content-between align-items-end">
      <b-button v-if="showForm" variant="outline-secondary" @click="showForm=!showForm">
        <i v-if="showForm" class="fas fa-toggle-off"></i> Back
      </b-button>
      <b-button v-else variant="outline-info" @click="showForm=!showForm">
        <i class="fas fa-toggle-on"></i> Update
      </b-button>
      <b-btn-group v-if="showForm">
        <b-button variant="outline-warning" type="reset">
          <i class="fas fa-eraser"></i> Reset
        </b-button>
        <b-button variant="success" type="subit" @click="changePoodle(formRef)">
          <i class="fas fa-save"></i> Save
        </b-button>
      </b-btn-group>
    </div>

  </div>
</template>

<script>
  import config from './../configuration.js'
  let perms = config.perms();
  export default {
    name: 'PoodleRegistration',
    props: [
      'poodle', 'formRef'
    ],
    data: function () {
      return {
        perms: perms,
        showForm: false
      }
    }
  }
</script>