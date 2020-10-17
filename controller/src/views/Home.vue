<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title id="tit">Bluetooth Scan</ion-title>
      </ion-toolbar>
    </ion-header>
    
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Bluetooth Scan</ion-title>
        </ion-toolbar>
      </ion-header>
    
      <div id="container">
        <ion-button v-on:click="init()">
          Init
        </ion-button>
        <ion-button v-on:click="startScan()">
          scan
        </ion-button>
      </div>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar, alertController } from '@ionic/vue';
import { defineComponent } from 'vue';
import { BluetoothLE } from '@ionic-native/bluetooth-le'

export default defineComponent({
  name: 'Home',
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
  },
  methods: {
    async init() {
        await BluetoothLE.initialize().subscribe(status => console.log(status));
    },
    async startScan() {
      const devices: {[index: string]: any} = {};
      BluetoothLE.startScan({}).subscribe(scanResult => {devices[scanResult.address] = scanResult.name});
      await new Promise(resolve => setTimeout(resolve, 5000));
      console.log(devices);
      console.log(await BluetoothLE.stopScan());

      let str = "";

      for (const key in devices) {
        if (Object.prototype.hasOwnProperty.call(devices, key)) {
          const name = devices[key];
          str += name + "\n";
        }
      }
      const alert = await alertController
        .create({
          cssClass: 'my-custom-class',
          header: 'Alert',
          subHeader: 'Subtitle',
          message: str,
          buttons: ['OK'],
        });
      return alert.present();
    }
  }
});
</script>

<style scoped>
#container {
  text-align: center;
  
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  
  color: #8c8c8c;
  
  margin: 0;
}

#container a {
  text-decoration: none;
}
</style>