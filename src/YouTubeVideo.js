import PropTypes from 'prop-types';
import React from 'react';

//import classes from 'styles/YouTubeVideo.module.css';

class YouTubeVideo extends React.PureComponent {
  static propTypes = {
    id: PropTypes.string.isRequired,
    start: PropTypes.string.isRequired,
    end: PropTypes.string.isRequired,
    onPointEnd: PropTypes.func
  };

  componentDidMount = () => {
    // On mount, check to see if the API script is already loaded
    this.props.ref.updateTimestamp = this.updateTimestamp;


    if (!window.YT) { // If not, load the script asynchronously
      const tag = document.createElement('script');
      tag.src = 'https://www.youtube.com/iframe_api';

      // onYouTubeIframeAPIReady will load the video after the script is loaded
      window.onYouTubeIframeAPIReady = this.loadVideo;

      const firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    } else { // If script is already there, load the video directly
      this.loadVideo();
    }
  };

  loadVideo = () => {
    const { id } = this.props;

    console.log("YT ID: " + id);
    console.log("Start: " + this.props.start);
    console.log("End: " + this.props.end);

    // the Player object is created uniquely based on the id in props
    this.player = new window.YT.Player(`youtube-player`, {
      videoId: id,
      events: {
        onReady: this.onPlayerReady,
        onStateChange: this.onPlayerStateChange
      },
    });
  };

  updateTimestamp = (timestamp) => {
    this.player.seekTo(timestamp, true);
  };

  updateId = (newId, start) => {
    this.player.loadVideoById(newId, start);
    console.log(`loaded new video ${newId} at ${start}`);
  };

  onPlayerReady = event => {
    console.log(this.props.start);
    event.target.seekTo(this.props.start, true);
    event.target.playVideo();

    console.log("set timer");
    this.currentPointTimer = setTimeout(
      () => this.props.onPointEnd(),
      this.getPointDuration(this.state.currentPoint)
    );
  };

  onPlayerStateChange = event => {
    if (event.data == 1) { //playing

    } else if (event.data == 2) { // paused

    }
  }

  render = () => {
    const { id } = this.props;
    return (
      <div >
        <div id={`youtube-player-${id}`} />
      </div>
    );
  };
}

export default YouTubeVideo;
