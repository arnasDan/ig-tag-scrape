import { Component, OnInit } from '@angular/core';
import { TagModel } from '../models/tag.model'
import { TagsService } from '../tags.service'

@Component({
  selector: 'app-popular-tags',
  templateUrl: './popular-tags.component.html',
  styleUrls: [
    './popular-tags.component.css'
  ]
})
export class PopularTagsComponent implements OnInit {
  popularTags = new Map();
  entries: any;
  loading: boolean = true;

  constructor(private itemsService: TagsService,) { }

  ngOnInit() {
    this.refreshList();
  }

  refreshList () {
    this.itemsService.getList().subscribe ((res: TagModel[]) => {
      this.loading = true;
      res.forEach(element => {
        let yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1);
        let timestamp = element.timestamp.length == 13 ? Number(element.timestamp) : Number(element.timestamp) * 1000;
        if (yesterday.getTime() < Number(element.timestamp) * 1000 || true) //ignore this for demonstration purposes.
        {
          if (this.popularTags.has(element.tag))
            this.popularTags.set(element.tag, this.popularTags.get(element.tag) + 1);
          else
            this.popularTags.set(element.tag, 1);
        }
      });
      this.entries = this.popularTags;
    });
    this.loading = false;
  }
  
  mapValues () {
    return Array.from(this.popularTags.entries()).sort((n1,n2)=> n2[1] - n1[1]).slice(0, 10);
  }

}
