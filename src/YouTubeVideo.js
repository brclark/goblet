import PropTypes from 'prop-types';
import React from 'react';

//import classes from 'styles/YouTubeVideo.module.css';

class YouTubeVideo extends React.PureComponent {
  static propTypes = {
    id: PropTypes.string.isRequired,
    start: PropTypes.string.isRequired,
    end: PropTypes.string.isRequired,
    inPointPlaylist: PropTypes.string.isRequired,
    onPointEnd: PropTypes.func
  };

  constructor(props) {
    super(props) {
      this.state = {
        remainingAfterPause: 0,
      }
    }
  }

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
      (this.props.end - this.props.start)*1000
    );
  };

  onPlayerStateChange = event => {
    if (event.data == 1) { //playing

    } else if (event.data == 2) { // paused
      if (this.state.inPointPlaylist) {
        this.setState({
          remaining: Date.now() - this.props.start,

        })
      }
    }
  }

  render = () => {
    return (
      <div>
        <div id={`youtube-player`} />
      </div>
    );
  };
}

export default YouTubeVideo;
