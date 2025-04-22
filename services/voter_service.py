from sqlalchemy.ext.asyncio import AsyncSession

class VoterService:

  async def create(self, db: AsyncSession, voter_entity: Voter)
