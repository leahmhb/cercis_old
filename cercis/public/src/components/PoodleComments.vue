  <template>
      <div id="comments">
          <article v-if=!showForm class="mt-2">
              <p v-if="poodle.comments">{{ poodle.comments }}</p>
              <p v-else>None</p>
          </article>
          <article v-else>
              <form :id="formRef" :ref="formRef" method="post"
                  @submit.prevent="changePoodle(formRef)">
                  <b-form-row>
                      <b-col>
                          <b-form-group label="Comments" label-for="comments" label-size="sm">
                              <b-form-textarea id="comments" v-model="poodle.comments" size="sm" trim></b-form-textarea>
                          </b-form-group>
                      </b-col>
                  </b-form-row>
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
          name: 'PoodleComments',
          props: [
              'poodle',
              'formRef'
          ],
          data: function () {
              return {
                  perms: perms,
                  showForm: false,
              }
          }
      }
  </script>