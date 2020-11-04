import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class YoutubeChannelService {

  constructor(private httpClient: HttpClient) { }

  getYoutubeChannelInfo() {
    return this.httpClient.get(environment.api_url + '/channel_info/');
  }
}
