import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home';
import { PredictionForm } from './components/prediction-form/prediction-form';
import { PredictionResult } from './components/prediction-result/prediction-result';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'predict', component: PredictionForm },
  { path: 'result', component: PredictionResult }
];