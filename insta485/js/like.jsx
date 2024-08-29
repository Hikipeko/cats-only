import React from "react";
import PropTypes from "prop-types";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart as solidHeart } from '@fortawesome/free-solid-svg-icons';
import { faHeart as regularHeart } from '@fortawesome/free-regular-svg-icons';


class Like extends React.Component {
  constructor(props) {
    super(props);
    // bind click events in constructor
    this.likeClick = this.likeClick.bind(this);
    this.unlikeClick = this.unlikeClick.bind(this);
  }

  likeClick() {
    const { postid, lognameLikesThis, numLikes, likeEvent } = this.props;
    console.log("like clicked in post:", postid, lognameLikesThis, numLikes);
    likeEvent();
  }

  unlikeClick() {
    const { postid, lognameLikesThis, numLikes, unlikeEvent } = this.props;
    console.log("unlike clicked in post:", postid, lognameLikesThis, numLikes);
    unlikeEvent();
  }

  render() {
    const { postid, lognameLikesThis, numLikes } = this.props;
    console.log(postid, lognameLikesThis, numLikes);
    return (
      <div>
        <div className="d-flex align-items-center">
          {lognameLikesThis ? (
            <UnlikeButton onClick={this.unlikeClick} />
          ) : (
            <LikeButton onClick={this.likeClick} />
          )}
        </div>
        <div className="mt-2">
          <p className="text-dark font-weight-bold" style={{ margin: '0 0 0 8px', fontSize: '12px' }}>
            {numLikes.toLocaleString()} {numLikes === 1 ? 'like' : 'likes'}
          </p>
        </div>
      </div>
    );
  }
}

Like.propTypes = {
  postid: PropTypes.number.isRequired,
  lognameLikesThis: PropTypes.bool.isRequired,
  numLikes: PropTypes.number.isRequired,
  likeEvent: PropTypes.func.isRequired,
  unlikeEvent: PropTypes.func.isRequired,
};

export default Like;

function LikeButton({ onClick }) {
  return (
    <button type="button" className="like-unlike-button" onClick={onClick} style={{ background: 'none', border: 'none', padding: '0' }}>
      <FontAwesomeIcon icon={regularHeart} style={{ color: '#262626', fontSize: '24px' }} />
    </button>
  );
}

LikeButton.propTypes = {
  onClick: PropTypes.func.isRequired,
};

function UnlikeButton({ onClick }) {
  return (
    <button type="button" className="like-unlike-button" onClick={onClick} style={{ background: 'none', border: 'none', padding: '0' }}>
      <FontAwesomeIcon icon={solidHeart} style={{ color: '#ed4956', fontSize: '24px' }} />
    </button>
  );
}

UnlikeButton.propTypes = {
  onClick: PropTypes.func.isRequired,
};
