
const healthCheckURL = "{% url 'dog_classifier_api_health_check' %}"
const authHealthCheckURL = "{% url 'dog_classifier_api_auth_health_check' %}"
const classifyURL = "{% url 'dog_classifier_api_classify' %}"


const app = new Vue({
    delimiters: ["[[", "]]"],
    el: "#dogApp",
    data: {
        
        dogImageFileUrl: null,
        dogBreedResult: null,
        rawDogBreedConfidenceScore: null,
        dogBreedConfidenceScore: null,
        
        dogClassifierAppLoading: false,
        
    },
    methods: {
        healthCheck: function(){
            axios.get(healthCheckURL).then(
                r => {
                    console.log(r)
                }
            ).catch(
                e => {
                    console.error(e)
                }
            )
            
        },
        authHealthCheck: function(){
            axios.get(authHealthCheckURL).then(
                r => {
                    console.log(r)
                }
            ).catch(
                e => {
                    console.error(e)
                }
            )
            
        },        
        classifyDog: function(){
            axios.post(classifyURL).then(
                r => {
                    console.log(r)
                    
                }
            ).catch(
                e => {
                    console.error(e)
                }
            )
            
        },
        changeUploadDogImageFile: function(e){
            let file = e.target.files[0]
            this.dogImageFileUrl = URL.createObjectURL(file)
            
        },
        
        uploadDogImageFile: function(){
            this.dogClassifierAppLoading = true
            console.log("dogImageFileUrl: " + this.dogImageFileUrl)
            console.log("upload")
            let formData = new FormData()
            formData.append('file', document.getElementById("uploadDogImageFile").files[0])

            axios.post(classifyURL, formData).then(
                r => {
                    this.dogBreedResult = r.data.dogBreedResult
                    this.rawDogBreedConfidenceScore = r.data.dogBreedConfidenceScore*100
                    this.dogBreedConfidenceScore = this.rawDogBreedConfidenceScore.toFixed(2)
                    this.dogClassifierAppLoading = false
                }
            ).catch(
                e => {
                    this.dogClassifierAppLoading = false
                    alert("Failed")
                    console.error(e)
                    
                }
            )
        },
        clearForm: function(){            
            this.dogImageFileUrl = null
            this.dogBreedResult = null
            this.dogBreedConfidenceScore = null
            this.dogClassifierAppLoading=false
        }
            

    },

    mounted:function(){
        //do this when mounted
        this.healthCheck()
        this.authHealthCheck()
    }

})