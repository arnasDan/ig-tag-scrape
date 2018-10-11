import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Router } from '@angular/router';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { PopularTagsComponent } from './popular-tags/popular-tags.component';
import { StatisticsComponent } from './statistics/statistics.component';
import { RandomTagComponent } from './random-tag/random-tag.component';

import { TagsService } from './tags.service'

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    PopularTagsComponent,
    StatisticsComponent,
    RandomTagComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    RouterModule.forRoot([
      {
          path: '',
          redirectTo: '/home',
          pathMatch: 'full'
      },
      {
        path: 'home',
        component: HomeComponent
      },
      {
        path: 'popular-tags',
        component: PopularTagsComponent
      },
      {
        path: 'statistics',
        component: StatisticsComponent
      },
      {
        path: 'random-tag',
        component: RandomTagComponent
      }
  ])
  ],
  providers: [
    TagsService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
