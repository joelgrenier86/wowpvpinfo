<template>
  <!-- <q-page padding :style="{ backgroundImage: `url(http://localhost:9000/src/assets/wow-pvp-bg.jpg)` }"> -->
    <q-page padding :style=bgImage>
    <div class="flex col" >
    <div class="row" style="width:100%">
      <div class="col-2">
        <q-list>
          <div v-for="(data, pk) in classes" :key="pk"  height="3%">
            <q-item
              :class="['bg-' + data.class_name]"
              @click="fetchSkills(data.class_name)"
             
              clickable
              v-ripple

            >
              <q-item-section avatar>
                <img :src="'src/assets/classicon_' + data.class_name +'.png'" style="height:36px"/>
              
              </q-item-section>

              <q-item-section>{{data.class_name}}</q-item-section>
            </q-item>
            <q-separator color="dark" />
          </div>
        </q-list>
      </div>
      <div class="col-2">
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
                  <img :src="'src/assets/icons/' + getSkillIcon(skill)" style="height:32px">
                </q-item-section>

                <q-item-section>{{skill.skill_name}}</q-item-section>
              </q-item>
              <q-separator color="dark" inset />
            </div>
          </div>
        </q-list>
      </div>
      
      <div class="col-8  dr-flex" v-if="!sharedDr || !sharedDr.length">
      </div>
      <div class="col-8  dr-flex" v-else>
      <div class="flex">
  
       
        


        
          <div>
            <div class = "row">
          
            <h3 class="text-center text-white shared-title" style="width:100%"> {{selectedSkill.skill_name}} shares DR with:</h3>
           </div>
            <div class="chip-box">
              
               
                  
              <q-chip v-for="skill in sharedDr" :key="skill.pk" :class="['bg-' + skill.class_name]" class="skill-chip text-left" text-color="black">
                <q-item-section avatar>
                <img :src="'src/assets/icons/' + getSkillIcon(skill)" style="height:32px">
              
              </q-item-section>
                
                {{skill.skill_name}}
              </q-chip>
                    
                  
               
                
                
                
            </div></div>
          
        
          </div> </div>
    </div></div></q-page>
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
                imageSrc:{type:String},
                bgColor:{type: String, default: "bg-grey-8"},
                selectedSkill:{},
            
               
               

                
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
                  this.selectedSkill = skill
                  api.get('skills?search=' + skill.dr_cat)
                      .then(response =>{
                      this.sharedDr = response.data
          
                    })
                    .catch(e => {
                      this.errors.push(e)
                    })
                    
                    
                    
                },
    
                
                getClassIcon(skill)
                  {
                
                    
                    return "~assets/classicon_" + skill.class_name +".jpg"
                  },   
                  getSkillIcon(skill)
                  {
                    return skill.skill_name.split(' ').join('') +".jpg"
                  }     
},
        computed:{
          bgImage() {
            return {backgroundImage: `url(http://localhost:9000/src/assets/wow-pvp-bg.jpg)`,
              backdropFilter: 'blur(10px)'
                    }
            },

        
          },

       created() {
                api.get('classes/')
                .then(response =>{
                  this.classes = response.data
                })
                .catch(e => {
                  this.errors.push(e)
                })
                .then(this.bgColor = "bg-grey-8")
               
            },
            


        }
   
        
  




</script>
