import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { YoutubeChannelComponent } from './youtube-channel/youtube-channel.component';

const routes: Routes = [
  { path: 'youtube-channel-data', component: YoutubeChannelComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
