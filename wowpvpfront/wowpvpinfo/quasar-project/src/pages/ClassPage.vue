<template>
  <q-page class="bg-grey-5" padding>
    <div class="row">
      <div class="col-2" :class="[bgColor]">
        <q-list>
          <div v-for="(data, pk) in classes" :key="pk">
            <q-item
              :class="['bg-' + data.class_name]"
              @click="fetchSkills(data.class_name)"
              clickable
              v-ripple
            >
              <q-item-section avatar>
                <q-avatar color="teal" text-color="white" icon="bluetooth" />
              </q-item-section>

              <q-item-section>{{data.class_name}}</q-item-section>
            </q-item>
            <q-separator color="dark" />
          </div>
        </q-list>
      </div>
      <div class="col-2" :class="[bgColor]">
        <q-list>
          <div v-if="skills">
            <div v-for="(skill, pk) in skills" :key="pk">
              <q-item
                :class="['bg-' + skill.class_name]"
                @click="fetchSharedDr(skill)"
                clickable
                v-ripple
              >
                <q-item-section avatar>
                  <q-avatar color="teal" text-color="white" icon="bluetooth" />
                </q-item-section>

                <q-item-section>{{skill.skill_name}}</q-item-section>
              </q-item>
              <q-separator color="dark" inset />
            </div>
          </div>
        </q-list>
      </div>
      <div class="col-8 bg-grey-9 flex">
        <q-list bordered style="width:100%">
          <div v-if="sharedDr">
            <div class="row">
            <div v-for="(skill, index) in sharedDr" :key="skill.pk" class = "col" style="width:50%" >
              
               
                  
                  <q-item
                    
                    :class="['bg-' + skill.class_name]"
                    clickable
                    v-ripple
                  >
                    <q-item-section avatar>
                      <q-avatar
                        color="teal"
                        text-color="white"
                        icon="bluetooth"
                      />
                    </q-item-section>

                    <q-item-section>{{skill.skill_name}} {{index}}</q-item-section>
                  </q-item>
         
                
                
                
            </div></div>
          </div></q-list>
        
      </div>
    </div></q-page
  >
</template>


<script>
import { ref } from 'vue'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'

export default {
  data() {
            return {
              
                classes: [],
                skills:[],
                sharedDr:[],
                bgColor:{type: String, default: "bg-dark"}
               
               

                
            }
        },
        methods:{
                  fetchSkills(class_name) {
                    this.sharedDr = []
                    this.bgColor = "bg-" + class_name
                    if(typeof skills === 'undefined' || class_name !== this.skills[0].class_name){
                  
                      api.get('skills?search=' + class_name)
                      .then(response =>{
                      this.skills = response.data
                    })
                    .catch(e => {
                      this.errors.push(e)
                    })
                  }
                },
                fetchSharedDr(skill){
                  api.get('skills?search=' + skill.dr_cat)
                      .then(response =>{
                      this.sharedDr = response.data
                    })
                    .catch(e => {
                      this.errors.push(e)
                    })
                }
        },
       created() {
                api.get('classes/')
                .then(response =>{
                  this.classes = response.data
                })
                .catch(e => {
                  this.errors.push(e)
                })
                .then(this.bgColor = "bg-dark")
               
            },
            


        }
   
        
  




</script>
