export interface ChannelInfo {
  channel_name: string;
  total_views: number;
  avg_num_of_views: number;
}

export interface ChannelInfoResponse {
  data: ChannelInfo;
  ok: boolean;
}
