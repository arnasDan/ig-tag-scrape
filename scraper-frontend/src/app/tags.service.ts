import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { TagModel } from './models/tag.model';

@Injectable()
export class TagsService {

  url = 'http://localhost:3000/tags';

  constructor(private http: Http) { }

  getList(): Observable<TagModel[]> {
    return this.http.get(this.url)
        .map((res: Response) => res.json() as any[])
        .catch((error: any) => Observable.throw(error));
  }

}