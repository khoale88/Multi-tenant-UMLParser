Comments.newComment {
  CommentFactory.newComment -> "the new comment" {
    Comment.<<create>> {
      IDGen.nextID -> newId;
      Transaction.add(this);
      Comments.getSize -> size;
    }
  Comments.addToCache(the new comment);
  }
}