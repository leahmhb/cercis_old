<template>
  <div id="health">
    <article v-if=!showForm class="mt-2">
      <div class="row">
        <div class="col">
          <table class="table table-sm">
            <tbody>
              <tr>
                <th>Hip Dysplasia</th>
                <td>{{ poodle.hip_clearance }}</td>
              </tr>
              <tr>
                <th>Patellar Luxation</th>
                <td>{{ poodle.patella_clearance }}</td>
              </tr>
              <tr>
                <th>Eye Examination</th>
                <td>{{ poodle.eye_clearance }}</td>
              </tr>
              <tr>
                <th>Von Willebrand Disease</th>
                <td>{{ poodle.vwd_clearance }}</td>
              </tr>
              <tr>
                <th>Legg-Calvé-Perthes Disease (LCP)</th>
                <td>{{ poodle.legg_c_p_clearance }}</td>
              </tr>
              <tr>
                <th>Sebaceous Adenitis (SA)</th>
                <td>{{ poodle.sa_clearance }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col">
          <table class="table table-sm">
            <tbody>
              <tr>
                <th>Elbow Dysplasia</th>
                <td>{{ poodle.elbow_clearance }}</td>
              </tr>
              <tr>
                <th>Cardiac Disease</th>
                <td>{{ poodle.heart_clearance }}</td>
              </tr>
              <tr>
                <th>Progressive Retinal Atrophy (PRA)</th>
                <td>{{ poodle.pra_optigen_clearance }}</td>
              </tr>
              <tr>
                <th>Thyroid</th>
                <td>{{ poodle.thyroid_clearance }}</td>
              </tr>
              <tr>
                <th>Neonatal Encephalopathy</th>
                <td>{{ poodle.neonatal_enceph_clearance }}</td>
              </tr>
              <tr>
                <th>Other</th>
                <td>{{ poodle.health_information }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </article>
    <article v-else>
      <form :id="formRef" :ref="formRef" method="post" @submit.prevent="changePoodle(formRef)">
      
            <b-form-group label="Hip Dysplasia" label-for="hip_clearance">
              <b-form-input id="hip_clearance" v-model="poodle.hip_clearance" trim></b-form-input>
            </b-form-group>
        
            <b-form-group label="Elbow Dysplasia" label-for="elbow_clearance">
              <b-form-input id="elbow_clearance" v-model="poodle.elbow_clearance" trim></b-form-input>
            </b-form-group>
 
            <b-form-group label="Patellar Luxation" label-for="patella_clearance">
              <b-form-input id="patella_clearance" v-model="poodle.patella_clearance" trim></b-form-input>
            </b-form-group>
       
            <b-form-group label="Cardiac Disease" label-for="heart_clearance">
              <b-form-input id="heart_clearance" v-model="poodle.heart_clearance" trim></b-form-input>
            </b-form-group>
        
            <b-form-group label="Eye Examination" label-for="eye_clearance">
              <b-form-input id="eye_clearance" v-model="poodle.eye_clearance" trim></b-form-input>
            </b-form-group>
        
            <b-form-group label="Progressive Retinal Atrophy (PRA)" label-for="pra_optigen_clearance">
              <b-form-input id="pra_optigen_clearance" v-model="poodle.pra_optigen_clearance" trim>
              </b-form-input>
            </b-form-group>
    
            <b-form-group label="Von Willebrand Disease" label-for="vwd_clearance">
              <b-form-input id="vwd_clearance" v-model="poodle.vwd_clearance" trim></b-form-input>
            </b-form-group>
   
            <b-form-group label="Thyroid" label-for="thyroid_clearance">
              <b-form-input id="thyroid_clearance" v-model="poodle.thyroid_clearance" trim></b-form-input>
            </b-form-group>
     
            <b-form-group label="Von Willebrand Disease" label-for="vwd_clearance">
              <b-form-input id="vwd_clearance" v-model="poodle.vwd_clearance" trim></b-form-input>
            </b-form-group>
         
            <b-form-group label="Thyroid" label-for="thyroid_clearance">
              <b-form-input id="thyroid_clearance" v-model="poodle.thyroid_clearance" trim></b-form-input>
            </b-form-group>
     
            <b-form-group label="Legg-Calvé-Perthes Disease (LCP)" label-for="legg_c_p_clearance">
              <b-form-input id="legg_c_p_clearance" v-model="poodle.legg_c_p_clearance" trim>
              </b-form-input>
            </b-form-group>
         
            <b-form-group label="Neonatal Encephalopathy" label-for="neonatal_enceph_clearance">
              <b-form-input id="neonatal_enceph_clearance" v-model="poodle.neonatal_enceph_clearance" trim>
              </b-form-input>
            </b-form-group>
    
            <b-form-group label="Sebaceous Adenitis (SA)" label-for="sa_clearance">
              <b-form-input id="sa_clearance" v-model="poodle.sa_clearance" trim></b-form-input>
            </b-form-group>
        
            <b-form-group label="Other" label-for="health_information">
              <b-form-input id="health_information" v-model="poodle.health_information" trim>
              </b-form-input>
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
                <b-button variant="outline-secondary" type="reset">
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
    name: 'PoodleHealth',
    props: [
      'poodle',
    ],
    data: function () {
      return {
        perms: perms,
        showForm: false,
      }
    }

  }
</script>