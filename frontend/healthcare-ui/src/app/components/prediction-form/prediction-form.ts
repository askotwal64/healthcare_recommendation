import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-prediction-form',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './prediction-form.html',
  styleUrl: './prediction-form.css'
})
export class PredictionForm {
}