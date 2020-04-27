import {planetScaleEnum as scaleEnum} from '../scaling.mjs';

export default class Dealer {

    constructor() {
        this.dealCards = () => {
            
            function shuffle(arra1) {
                var ctr = arra1.length, temp, index;
              
              // While there are elements in the array
                while (ctr > 0) {
              // Pick a random index
                    index = Math.floor(Math.random() * ctr);
              // Decrease ctr by 1
                    ctr--;
              // And swap the last element with it
                    temp = arra1[ctr];
                    arra1[ctr] = arra1[index];
                    arra1[index] = temp;
                }
                return arra1;
              }

              let planets = shuffle(Object.values(scaleEnum).splice(1,8));

                return planets;
        }
    }
}