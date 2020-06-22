  <template>
      <div id="comments">
          <article v-if=!showCommentsForm class="mt-2">
              <p v-if="poodle.comments">{{ poodle.comments }}</p>
              <p v-else>None</p>
          </article>
          <article v-else>
              <form id="comments-form" ref="comments-form" method="post"
                  @submit.prevent="changePoodle('comments-form')">
                  <b-form-row>
                      <b-col>
                          <b-form-group label="Comments" label-for="comments" label-size="sm">
                              <b-form-textarea id="comments" v-model="poodle.comments" size="sm" trim></b-form-textarea>
                          </b-form-group>
                      </b-col>
                  </b-form-row>
              </form>
          </article>

          <div v-if="perms.core.change_poodle"
              class="mt-4 mb-0 d-flex flex-row justify-content-between align-items-end">
              <b-button variant="outline-info" @click="showCommentsForm=!showCommentsForm">
                  <i v-if="showCommentsForm" class="fas fa-toggle-off"></i>
                  <i v-else class="fas fa-toggle-on"></i> Update
              </b-button>
              <b-btn-group v-if="showCommentsForm">
                  <b-button variant="outline-secondary" type="reset">
                      <i class="fas fa-eraser"></i> Reset
                  </b-button>
                  <b-button variant="success" type="subit" @click="changePoodle('comments-form')">
                      <i class="fas fa-save"></i> Save
                  </b-button>
              </b-btn-group>
          </div>

      </div>
  </template>

  <script>
      import config from './../configuration.js'
      let perms = config.endpoints.perms();
      export default {
          name: 'PoodleComments',
          props: [
              'poodle',
              'showCommentsForm'
          ],
          data: function () {
              return {
                  perms: perms
              }
          }
      }
  </script>