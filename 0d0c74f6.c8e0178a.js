(window.webpackJsonp=window.webpackJsonp||[]).push([[2],{124:function(e,t,a){var n=a(125);e.exports=function(e,t){if(e){if("string"==typeof e)return n(e,t);var a=Object.prototype.toString.call(e).slice(8,-1);return"Object"===a&&e.constructor&&(a=e.constructor.name),"Map"===a||"Set"===a?Array.from(e):"Arguments"===a||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a)?n(e,t):void 0}},e.exports.default=e.exports,e.exports.__esModule=!0},125:function(e,t){e.exports=function(e,t){(null==t||t>e.length)&&(t=e.length);for(var a=0,n=new Array(t);a<t;a++)n[a]=e[a];return n},e.exports.default=e.exports,e.exports.__esModule=!0},126:function(e){e.exports=JSON.parse('[{"title":"Deep Learning"},{"title":"Machine Learning"},{"title":"NLP"},{"title":"Design"}]')},80:function(e,t,a){"use strict";a.r(t);var n=a(3),r=a(124);var i=a(0),o=a.n(i),s=a(83),l=a(88),c=(a(85),a(22)),m=a(86),u=a(56),d=a.n(u),p=a(93),g=a(126);function h(e){var t=e.imageUrl,a=e.title,n=e.semester,r=e.students,i=e.description,l=e.project_link,c=Object(m.a)(t);return o.a.createElement("div",{className:Object(s.a)("col col--4",d.a.projects)},o.a.createElement("div",{className:(Object(s.a)("card"),d.a.proj_card)},o.a.createElement("div",{className:d.a.card_img},c&&o.a.createElement("div",{className:"text--center"},o.a.createElement("img",{className:d.a.featureImage,src:c,alt:a}))),o.a.createElement("div",{className:d.a.card_body},o.a.createElement("h3",null,a," (",n,")"),o.a.createElement("p",{className:"proj_students"},o.a.createElement("i",null,r)),o.a.createElement("p",{className:"proj_descr"},i),o.a.createElement("div",{className:"button-group button-group--block"},l&&o.a.createElement("a",{className:"button button--small button--secondary button--block",href:l,target:"_blank",rel:"noreferrer noopener"},"Check out the Project!")))))}function f(){for(var e,t=[],a=function(e,t){var a;if("undefined"==typeof Symbol||null==e[Symbol.iterator]){if(Array.isArray(e)||(a=r(e))||t&&e&&"number"==typeof e.length){a&&(e=a);var n=0;return function(){return n>=e.length?{done:!0}:{done:!1,value:e[n++]}}}throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}return(a=e[Symbol.iterator]()).next.bind(a)}(g);!(e=a()).done;){var n=e.value;t.push(o.a.createElement("button",{className:"button button--small button--primary button--block",key:g.title},n.title))}return o.a.createElement("div",{className:"button-group button-group--block"},t)}t.default=function(){return Object(c.default)().siteConfig,o.a.createElement(l.a,{title:"Deep Learning Projects",description:"Projects from the Deep Learning Course @ Opencampus"},o.a.createElement("main",{className:"container margin-vert--lg"},o.a.createElement("div",{className:"text--center"},o.a.createElement("h1",null,"Deep Learning Projects"),o.a.createElement("p",null,"See the awesome projects people finished during the course"),o.a.createElement("div",{className:"buttons"},o.a.createElement(f,null))),p.a&&p.a.length>0&&o.a.createElement("section",{className:d.a.features},o.a.createElement("div",{className:"container"},o.a.createElement("div",{className:"row"},p.a.map((function(e,t){return o.a.createElement(h,Object(n.a)({key:t},e))})))))))}},93:function(e,t,a){"use strict";var n=a(0),r=a.n(n);const i="https://github.com/opencampus-sh/ML-Projects/blob/main/src/data/dl/code/",o=[{title:"COVID-19 Detection on X-Ray Image",imageUrl:"img/dl/COVID-19-Xray-Image-ClassificationProject.PNG",semester:"WiSe 20/21",students:"Mithun Das, Mohammad Wasif Islam, Rakibuzzaman Mahmud, Sarker Miraz Mahfuz",description:r.a.createElement(r.a.Fragment,null,"Can we detect COVID from an X-Ray image of the lungs? It turns out we can, or better, a software can do that for us. This project achieved an accuracy of 0.9896 on this task!"),project_link:i+"COVID-19-Xray-Image-Classification"},{title:"Face Mask Recognition",imageUrl:"img/dl/DeepLearningFaceMaskRecognitionProject.PNG",semester:"WiSe 20/21",students:"Adnan Nooruddin, Ravish Kumar, Christoph Eberz, Bennet M\xf6ller",description:r.a.createElement(r.a.Fragment,null,"This project develops a detection system which tells from a picture whether the person is wearing a mask or not."),project_link:i+"FaceMaskRecognition"},{title:"Painting Classification",imageUrl:"img/dl/PaintingClassificationProject.PNG",semester:"WiSe 20/21",students:"John Jay Kimani, Nils Berns",description:r.a.createElement(r.a.Fragment,null,"Which artist painted this painting? Nils and John tried to answer this question using neural networks with different approaches, discover more in their presentation."),project_link:i+"PaintingClassification"},{title:"Bike Sharing Prediction (SprottenFlotte)",imageUrl:"img/dl/BikeSharingPredictionProject.png",semester:"WiSe 20/21",students:"Andrej Ponomarenko, Daniel Michells",description:r.a.createElement(r.a.Fragment,null,"Analyzing the SprottenFlotte data from Kiel, can we predict where will the next bike be borrowed? ",r.a.createElement("i",null,r.a.createElement("b",null,"Note"),": the data for this project is private and cannot be shared, only the results.")),project_link:i+"BikeSharingPrediction"},{title:"Disease Classification on Medical XRay Images",imageUrl:"img/dl/DiseaseClassificationXRayProject.PNG",semester:"WiSe 20/21",students:"Sudesh Acharya",description:r.a.createElement(r.a.Fragment,null,"Can a neural network distinguish different types of diseases just by looking at a single X-Ray image of the lungs? The project shows promising results in this direction."),project_link:i+"DiseaseClassificationXRay"},{title:"Windfinder Predictions",imageUrl:"img/dl/WindfinderProject.png",semester:"WiSe 20/21",students:"Lennart Petersen",description:r.a.createElement(r.a.Fragment,null,"Predicting the best spot for surfing is a hard task, yet Lennart gave it a great shot and developed a model to predict it with 86% of accuracy. ",r.a.createElement("i",null,r.a.createElement("b",null,"Note"),": the data for this project is private and cannot be shared, only the results.")),project_link:i+"windfinderNN.ipynb"},{title:"Image Segmentation",imageUrl:"img/dl/ImageSegmentationProject.PNG",semester:"WiSe 20/21",students:"Yi-Jie Yang, Sebastian Koch, Erwin Smith, Suman Singha",description:r.a.createElement(r.a.Fragment,null,"Segmentation is used to separate an object from the background. Using a U-Net the group was able to do some interesting work on a Kaggle Challenge."),project_link:i+"ImageSegmentation"}];t.a=o}}]);