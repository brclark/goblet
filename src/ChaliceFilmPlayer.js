import React from 'react';
import YouTubeVideo from './YouTubeVideo'

class ChaliceFilmPlayer extends React.Component {
  constructor(props) {
    super(props);
    this.youtubeRef = React.createRef();
    this.state = {
      points: [],
      currentIndex: 0,
      currentPoint: null
    };
  }

  getPointDuration(point) {
    return (point["youtube_end"] - point["youtube_start"])*1000;
  }

  youtubeParser(url) {
    var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
    var match = url.match(regExp);
    return (match&&match[7].length===11)? match[7] : false;
  }

  currentId() {
    if (!this.state.currentPoint) return "";
    return this.youtubeParser(this.state.currentPoint["game"]["youtube_url"]);
  }

  componentDidMount() {
    fetch('http://localhost:5000/points/1').then(res => res.json()).then(
      data => {
        this.setState({
          points: [data],
          currentIndex: 0,
          currentPoint: data
        })
      });
  }

  setPointsPlaylist = (points, pointId = -1) => {

    let startIndex = (pointId !== -1) ? points.map(e => {
        return e.id
      }).indexOf(pointId) : 0;

    this.setState({
      points: points,
      currentIndex: startIndex,
      currentPoint: points[startIndex],
    });
  }

  nextPoint = () => {
    let previousPointId = this.currentId();
    let nextIndex = (this.state.currentIndex + 1) % this.state.points.length;
    console.log("next point index " + nextIndex);
    this.setState({
      currentIndex: nextIndex,
      currentPoint: this.state.points[nextIndex]
    });

    // Possibly update YouTube video id, as well as timestamp of new point
    // if (previousPointId !== this.currentId()) {
    //   this.youtubeRef.updateId(this.currentId());
    // }
    // this.youtubeRef.updateTimestamp(this.state.currentPoint["youtube_start"]);

  }

  render() {
    let start = this.state.currentPoint !== null ?
        this.state.currentPoint["youtube_start"] : "0";

    let end = this.state.currentPoint !== null ?
        this.state.currentPoint["youtube_end"] : "0";

    if (!this.state.currentPoint) {
      return (<div />);
    }

    return (
      <YouTubeVideo id={this.currentId()}
                    start={start} end={end} onPointEnd={this.nextPoint} />
    );
  }
}

export default ChaliceFilmPlayer
