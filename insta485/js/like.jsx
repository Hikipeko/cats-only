import React from "react";
import PropTypes from "prop-types";

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
        <div className="row">
          <div className="col-md-8 mt-1">
            <p>
              {numLikes}
              {numLikes === 1 ? " like" : " likes"}
            </p>
          </div>
        </div>
        <div>
          {lognameLikesThis ? (
            <UnlikeButton onClick={this.unlikeClick} />
          ) : (
            <LikeButton onClick={this.likeClick} />
          )}
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

function LikeButton(props) {
  const { onClick } = props;
  return (
    <button type="button" className="like-unlike-button" onClick={onClick}>
      Like
    </button>
  );
}

LikeButton.propTypes = {
  onClick: PropTypes.func.isRequired,
};

function UnlikeButton(props) {
  const { onClick } = props;
  return (
    <button type="button" className="like-unlike-button" onClick={onClick}>
      Unlike
    </button>
  );
}

UnlikeButton.propTypes = {
  onClick: PropTypes.func.isRequired,
};
