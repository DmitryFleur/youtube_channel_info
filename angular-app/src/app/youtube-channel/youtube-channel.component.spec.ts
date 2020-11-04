import { ComponentFixture, TestBed } from '@angular/core/testing';

import { YoutubeChannelComponent } from './youtube-channel.component';

describe('YoutubeChannelComponent', () => {
  let component: YoutubeChannelComponent;
  let fixture: ComponentFixture<YoutubeChannelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ YoutubeChannelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(YoutubeChannelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
