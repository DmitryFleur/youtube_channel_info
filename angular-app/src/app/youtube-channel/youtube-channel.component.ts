import { Component, OnInit } from '@angular/core';
import { ChannelInfo, ChannelInfoResponse } from '../interfaces/channel-info';
import { YoutubeChannelService } from './youtube-channel.service';

@Component({
  selector: 'app-youtube-channel',
  templateUrl: './youtube-channel.component.html',
  styleUrls: ['./youtube-channel.component.css']
})
export class YoutubeChannelComponent implements OnInit {

  youtubeData: ChannelInfo = {
    channel_name: null,
    total_views: 0,
    avg_num_of_views: 0
  };

  constructor(public youtubeChannelService: YoutubeChannelService) { }

  ngOnInit(): void {
    this.getYoutubeData();
  }

  getYoutubeData() {
    this.youtubeChannelService.getYoutubeChannelInfo().subscribe((data: ChannelInfoResponse) => {
      this.youtubeData = data.data;
    });
  }

}
